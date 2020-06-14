%global packname  optBiomarker
%global packver   1.0-27
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.27
Release:          2%{?dist}
Summary:          Estimation of optimal number of biomarkers for two-groupmicroarray based classifications at a given error tolerancelevel for various classification rules

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-rpanel 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-ipred 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-rpanel 
Requires:         R-CRAN-rgl 
Requires:         R-MASS 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-ipred 
Requires:         R-CRAN-msm 
Requires:         R-Matrix 

%description
Estimates optimal number of biomarkers for two-group classification based
on microarray data

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
