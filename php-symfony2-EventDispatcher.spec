%define		package	EventDispatcher
%define		php_min_version 5.3.9
Summary:	Symfony2 EventDispatcher Component
Name:		php-symfony2-EventDispatcher
Version:	2.8.52
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{package}/archive/v%{version}/%{package}-%{version}.tar.gz
# Source0-md5:	ad1d4eaded4416429c39f5b57af7f50a
URL:		https://symfony.com/doc/2.8/components/event_dispatcher.htmlindex.html
BuildRequires:	phpab
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(spl)
Requires:	php-dirs >= 1.6
Suggests:	php-symfony2-DependencyInjection
Suggests:	php-symfony2-HttpKernel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Implements a lightweight version of the Observer design pattern.

%prep
%setup -q -n event-dispatcher-%{version}

%build
phpab -n -e '*/Tests/*' -o autoload.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
cp -a *.php */ $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
rm -r $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}/Tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_data_dir}/Symfony/Component/EventDispatcher
%{php_data_dir}/Symfony/Component/EventDispatcher/*.php
%{php_data_dir}/Symfony/Component/EventDispatcher/Debug
%{php_data_dir}/Symfony/Component/EventDispatcher/DependencyInjection
