%global __brp_check_rpaths %{nil}
%global packname  gtop
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Game-Theoretically OPtimal (GTOP) Reconciliation Method

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-hts 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-lassoshooting 
Requires:         R-CRAN-hts 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-lassoshooting 

%description
In hierarchical time series (HTS) forecasting, the hierarchical relation
between multiple time series is exploited to make better forecasts. This
hierarchical relation implies one or more aggregate consistency
constraints that the series are known to satisfy. Many existing
approaches, like for example bottom-up or top-down forecasting, therefore
attempt to achieve this goal in a way that guarantees that the forecasts
will also be aggregate consistent. This package provides with an
implementation of the Game-Theoretically OPtimal (GTOP) reconciliation
method proposed in van Erven and Cugliari (2015), which is guaranteed to
only improve any given set of forecasts. This opens up new possibilities
for constructing the forecasts. For example, it is not necessary to assume
that bottom-level forecasts are unbiased, and aggregate forecasts may be
constructed by regressing both on bottom-level forecasts and on other
covariates that may only be available at the aggregate level.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
