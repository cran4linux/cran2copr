%global __brp_check_rpaths %{nil}
%global packname  ALTopt
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Optimal Experimental Designs for Accelerated Life Testing

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cubature >= 1.0
BuildRequires:    R-lattice >= 0.20
BuildRequires:    R-methods 
Requires:         R-CRAN-cubature >= 1.0
Requires:         R-lattice >= 0.20
Requires:         R-methods 

%description
Creates the optimal (D, U and I) designs for the accelerated life testing
with right censoring or interval censoring. It uses generalized linear
model (GLM) approach to derive the asymptotic variance-covariance matrix
of regression coefficients. The failure time distribution is assumed to
follow Weibull distribution with a known shape parameter and log-linear
link functions are used to model the relationship between failure time
parameters and stress variables. The acceleration model may have multiple
stress factors, although most ALTs involve only two or less stress
factors. ALTopt package also provides several plotting functions including
contour plot, Fraction of Use Space (FUS) plot and Variance Dispersion
graphs of Use Space (VDUS) plot. For more details, see Seo and Pan (2015)
<doi:10.32614/RJ-2015-029>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
