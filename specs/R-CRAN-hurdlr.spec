%global __brp_check_rpaths %{nil}
%global packname  hurdlr
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Zero-Inflated and Hurdle Modelling Using Bayesian Inference

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch

%description
When considering count data, it is often the case that many more zero
counts than would be expected of some given distribution are observed. It
is well established that data such as this can be reliably modelled using
zero-inflated or hurdle distributions, both of which may be applied using
the functions in this package. Bayesian analysis methods are used to best
model problematic count data that cannot be fit to any typical
distribution. The package functions are flexible and versatile, and can be
applied to varying count distributions, parameter estimation with or
without explanatory variable information, and are able to allow for
multiple hurdles as it is also not uncommon that count data have an
abundance of large-number observations which would be considered outliers
of the typical distribution. In lieu of throwing out data or misspecifying
the typical distribution, these extreme observations can be applied to a
second, extreme distribution. With the given functions of this package,
such a two-hurdle model may be easily specified in order to best manage
data that is both zero-inflated and over-dispersed.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
