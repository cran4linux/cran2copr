%global packname  mclcar
%global packver   0.1-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.9
Release:          1%{?dist}
Summary:          Estimating Conditional Auto-Regressive (CAR) Models using MonteCarlo Likelihood Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-CRAN-rsm 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-spdep 
Requires:         R-CRAN-spam 
Requires:         R-CRAN-rsm 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-spdep 

%description
The likelihood of direct CAR models and Binomial and Poisson GLM with
latent CAR variables are approximated by the Monte Carlo likelihood. The
Maximum Monte Carlo likelihood estimator is found either by an iterative
procedure of directly maximising the Monte Carlo approximation or by a
response surface design method.Reference for the method can be found in
the DPhil thesis in Z. Sha (2016). For application a good reference is
R.Bivand et.al (2017) <doi:10.1016/j.spasta.2017.01.002>.

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
