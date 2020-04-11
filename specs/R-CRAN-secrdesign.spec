%global packname  secrdesign
%global packver   2.5.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5.11
Release:          1%{?dist}
Summary:          Sampling Design for Spatially Explicit Capture-Recapture

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-secr >= 3.2.0
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-openCR 
Requires:         R-CRAN-secr >= 3.2.0
Requires:         R-parallel 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-openCR 

%description
Tools for designing spatially explicit capture-recapture studies of animal
populations. This is primarily a simulation manager for package 'secr'.
Extensions in version 2.5.0 include costing and evaluation of detector
spacing.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
