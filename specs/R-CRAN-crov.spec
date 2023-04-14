%global __brp_check_rpaths %{nil}
%global packname  crov
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Constrained Regression Model for an Ordinal Response and OrdinalPredictors

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gtools >= 3.5.0
BuildRequires:    R-stats >= 3.4.3
BuildRequires:    R-CRAN-VGAM >= 1.0.5
Requires:         R-CRAN-gtools >= 3.5.0
Requires:         R-stats >= 3.4.3
Requires:         R-CRAN-VGAM >= 1.0.5

%description
Fits a constrained regression model for an ordinal response with ordinal
predictors and possibly others, Espinosa and Hennig (2019)
<doi:10.1007/s11222-018-9842-2>. The parameter estimates associated with
an ordinal predictor are constrained to be monotonic. If a monotonicity
direction (isotonic or antitonic) is not specified for an ordinal
predictor by the user, then the monotonicity direction classification
procedure establishes it. Two monotonicity tests are also available to
test the null hypothesis of monotonicity over a set of parameters
associated with an ordinal predictor.

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
%{rlibdir}/%{packname}
