%global packname  convoSPAT
%global packver   1.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.6
Release:          1%{?dist}
Summary:          Convolution-Based Nonstationary Spatial Modeling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-StatMatch 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-fields 
Requires:         R-MASS 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-StatMatch 

%description
Fits convolution-based nonstationary Gaussian process models to
point-referenced spatial data. The nonstationary covariance function
allows the user to specify the underlying correlation structure and which
spatial dependence parameters should be allowed to vary over space: the
anisotropy, nugget variance, and process variance. The parameters are
estimated via maximum likelihood, using a local likelihood approach. Also
provided are functions to fit stationary spatial models for comparison,
calculate the Kriging predictor and standard errors, and create various
plots to visualize nonstationarity.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
