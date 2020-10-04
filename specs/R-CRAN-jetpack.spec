%global packname  jetpack
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          3%{?dist}%{?buildtag}
Summary:          A Friendly Package Manager

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-remotes >= 2.0.3
BuildRequires:    R-CRAN-desc >= 1.2.0
BuildRequires:    R-CRAN-crayon >= 1.0.0
BuildRequires:    R-CRAN-packrat >= 0.4.9
BuildRequires:    R-CRAN-docopt >= 0.4
Requires:         R-CRAN-remotes >= 2.0.3
Requires:         R-CRAN-desc >= 1.2.0
Requires:         R-CRAN-crayon >= 1.0.0
Requires:         R-CRAN-packrat >= 0.4.9
Requires:         R-CRAN-docopt >= 0.4

%description
Manage project dependencies from your DESCRIPTION file. Create a
reproducible virtual environment with minimal additional files in your
project. Provides tools to add, remove, and update dependencies as well as
install existing dependencies with a single function.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
