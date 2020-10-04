%global packname  rbundler
%global packver   0.3.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.7
Release:          3%{?dist}%{?buildtag}
Summary:          Rbundler manages an application's dependencies systematicallyand repeatedly.

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-CRAN-devtools >= 1.3
Requires:         R-CRAN-devtools >= 1.3

%description
Rbundler manages a project-specific library for dependency package
installation. By specifying dependencies in a DESCRIPTION file in a
project's root directory, one may install and use dependencies in a
repeatable fashion without requiring manual maintenance. rbundler creates
a project-specific R library in `PROJECT_ROOT/.Rbundle` (by default) and a
project-specific `R_LIBS_USER` value, set in `PROJECT_ROOT/.Renviron`. It
supports dependency management for R standard "Depends", "Imports",
"Suggests", and "LinkingTo" package dependencies. rbundler also attempts
to validate and install versioned dependencies, such as ">=", "==", "<=".
Note that, due to the way R manages package installation, differing nested
versioned dependencies are not allowed. For example, if your project
depends on packages A (== 1), and B (== 2), but package A depends on B (==
1), then a nested dependency violation will cause rbundler to error out.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
