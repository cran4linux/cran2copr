%global packname  scoringutils
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Utilities for Scoring and Assessing Predictions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-goftest 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-scoringRules 
BuildRequires:    R-stats 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-goftest 
Requires:         R-graphics 
Requires:         R-CRAN-scoringRules 
Requires:         R-stats 

%description
Combines a collection of metrics and proper scoring rules (Tilmann
Gneiting & Adrian E Raftery (2007) <doi:10.1198/016214506000001437>) with
an easy to use wrapper that can be used to automatically evaluate
predictions. Apart from proper scoring rules functions are provided to
assess bias, sharpness and calibration (Sebastian Funk, Anton Camacho,
Adam J. Kucharski, Rachel Lowe, Rosalind M. Eggo, W. John Edmunds (2019)
<doi:10.1371/journal.pcbi.1006785>) of forecasts. Several types of
predictions can be evaluated: probabilistic forecasts (generally
predictive samples generated by Markov Chain Monte Carlo procedures),
quantile forecasts or point forecasts. Observed values and predictions can
be either continuous, integer, or binary. Users can either choose to apply
these rules separately in a vector / matrix format that can be flexibly
used within other packages, or they can choose to do an automatic
evaluation of their forecasts. This is implemented with 'data.table' and
provides a consistent and very efficient framework for evaluating various
types of predictions.

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
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX