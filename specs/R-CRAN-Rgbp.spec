%global packname  Rgbp
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          2%{?dist}
Summary:          Hierarchical Modeling and Frequency Method Checking onOverdispersed Gaussian, Poisson, and Binomial Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.2.0
Requires:         R-core >= 2.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-mnormt 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-mnormt 

%description
We utilize approximate Bayesian machinery to fit two-level conjugate
hierarchical models on overdispersed Gaussian, Poisson, and Binomial data
and evaluates whether the resulting approximate Bayesian interval
estimates for random effects meet the nominal confidence levels via
frequency coverage evaluation. The data that Rgbp assumes comprise
observed sufficient statistic for each random effect, such as an average
or a proportion of each group, without population-level data.  The
approximate Bayesian tool equipped with the adjustment for density
maximization produces approximate point and interval estimates for model
parameters including second-level variance component, regression
coefficients, and random effect. For the Binomial data, the package
provides an option to produce posterior samples of all the model
parameters via the acceptance-rejection method. The package provides a
quick way to evaluate coverage rates of the resultant Bayesian interval
estimates for random effects via a parametric bootstrapping, which we call
frequency method checking.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
