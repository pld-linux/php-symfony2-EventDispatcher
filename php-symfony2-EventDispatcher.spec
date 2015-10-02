%define		package	EventDispatcher
%define		php_min_version 5.3.9
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 EventDispatcher Component
Name:		php-symfony2-EventDispatcher
Version:	2.7.5
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{package}/archive/v%{version}/%{package}-%{version}.tar.gz
# Source0-md5:	76eb287f1a2f19a309325c51c2c2ed16
URL:		http://symfony.com/doc/2.7/components/event_dispatcher/index.html
BuildRequires:	phpab
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(spl)
Requires:	php-pear >= 4:1.3.10
Suggests:	php-symfony2-DependencyInjection
Suggests:	php-symfony2-HttpKernel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Implements a lightweight version of the Observer design pattern.

%prep
%setup -q -n event-dispatcher-%{version}

%build
phpab -n -e '*/Tests/*' -o autoloader.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{package}
cp -a *.php */ $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{package}
rm -r $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{package}/Tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_pear_dir}/Symfony/Component/EventDispatcher
%{php_pear_dir}/Symfony/Component/EventDispatcher/*.php
%{php_pear_dir}/Symfony/Component/EventDispatcher/Debug
%{php_pear_dir}/Symfony/Component/EventDispatcher/DependencyInjection
