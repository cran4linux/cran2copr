%global packname  vows
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          3%{?dist}%{?buildtag}
Summary:          Voxelwise Semiparametrics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.9.0
Requires:         R-core >= 2.9.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-gamm4 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-RLRsim 
BuildRequires:    R-CRAN-oro.nifti 
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-gamm4 
Requires:         R-mgcv 
Requires:         R-CRAN-RLRsim 
Requires:         R-CRAN-oro.nifti 
Requires:         R-CRAN-shape 
Requires:         R-CRAN-stringr 

%description
Parametric and semiparametric inference for massively parallel models,
i.e., a large number of models with common design matrix, as often occurs
with brain imaging data.

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
%{rlibdir}/%{packname}/INDEX
