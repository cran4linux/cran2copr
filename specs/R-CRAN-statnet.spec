%global packname  statnet
%global packver   2019.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2019.6
Release:          3%{?dist}%{?buildtag}
Summary:          Software Tools for the Statistical Analysis of Network Data

License:          GPL-3 + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-statnet.common >= 4.2
BuildRequires:    R-CRAN-tergm >= 3.6.1
BuildRequires:    R-CRAN-ergm.count >= 3.3
BuildRequires:    R-CRAN-ergm >= 3.10.4
BuildRequires:    R-CRAN-sna >= 2.4
BuildRequires:    R-CRAN-network >= 1.15
BuildRequires:    R-CRAN-tsna >= 0.3
BuildRequires:    R-CRAN-networkDynamic >= 0.10.0
Requires:         R-CRAN-statnet.common >= 4.2
Requires:         R-CRAN-tergm >= 3.6.1
Requires:         R-CRAN-ergm.count >= 3.3
Requires:         R-CRAN-ergm >= 3.10.4
Requires:         R-CRAN-sna >= 2.4
Requires:         R-CRAN-network >= 1.15
Requires:         R-CRAN-tsna >= 0.3
Requires:         R-CRAN-networkDynamic >= 0.10.0

%description
Statnet is a collection of packages for statistical network analysis that
are designed to work together because they share common data
representations and 'API' design.  They provide an integrated set of tools
for the representation, visualization, analysis, and simulation of many
different forms of network data. This package is designed to make it easy
to install and load the key 'statnet' packages in a single step.  Learn
more about 'statnet' at <http://www.statnet.org>.  Tutorials for many
packages can be found at <https://github.com/statnet/Workshops/wiki>.  For
an introduction to functions in this package, type
help(package='statnet').

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
