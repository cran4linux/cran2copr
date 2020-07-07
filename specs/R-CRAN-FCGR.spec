%global packname  FCGR
%global packver   1.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Fatigue Crack Growth in Reliability

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-KernSmooth 
BuildRequires:    R-CRAN-kerdiest 
BuildRequires:    R-nlme 
BuildRequires:    R-MASS 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-pspline 
BuildRequires:    R-CRAN-sfsmisc 
Requires:         R-KernSmooth 
Requires:         R-CRAN-kerdiest 
Requires:         R-nlme 
Requires:         R-MASS 
Requires:         R-mgcv 
Requires:         R-CRAN-pspline 
Requires:         R-CRAN-sfsmisc 

%description
Fatigue Crack Growth in Reliability estimates the distribution of material
lifetime due to mechanical fatigue efforts. The FCGR package provides
simultaneous crack growth curves fitting to different specimens in
materials under mechanical stress efforts. Linear mixed-effects models
(LME) with smoothing B-Splines and the linearized Paris-Erdogan law are
applied. Once defined the fail for a determined crack length, the
distribution function of failure times to fatigue is obtained. The density
function is estimated by applying nonparametric binned kernel density
estimate (bkde) and the kernel estimator of the distribution function
(kde). The results of Pinheiro and Bates method based on nonlinear
mixed-effects regression (nlme) can be also retrieved. The package
contains the crack.growth, PLOT.cg, IB.F, and Alea.A (database) functions.

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
