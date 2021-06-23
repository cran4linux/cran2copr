%global __brp_check_rpaths %{nil}
%global packname  marcher
%global packver   0.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Migration and Range Change Estimation in R

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-Matrix 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-scales 
Requires:         R-stats 
Requires:         R-Matrix 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-scales 

%description
A set of tools for likelihood-based estimation, model selection and
testing of two- and three-range shift and migration models for animal
movement data as described in Gurarie et al. (2017) <doi:
10.1111/1365-2656.12674>.  Provided movement data (X, Y and Time),
including irregularly sampled data, functions estimate the time, duration
and location of one or two range shifts, as well as the ranging area and
auto-correlation structure of the movment.  Tests assess, for example,
whether the shift was "significant", and whether a two-shift migration was
a true return migration.

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
%{rlibdir}/%{packname}/data
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
