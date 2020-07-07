%global packname  ASSISTant
%global packver   1.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.2
Release:          3%{?dist}
Summary:          Adaptive Subgroup Selection in Group Sequential Trials

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 

%description
Clinical trial design for subgroup selection in three-stage group
sequential trial. Includes facilities for design, exploration and analysis
of such trials. An implementation of the initial DEFUSE-3 trial is also
provided as a vignette.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/full_doc
%{rlibdir}/%{packname}/INDEX
