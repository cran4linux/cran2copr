%global packname  WeightIt
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}
Summary:          Weighting for Covariate Balance in Observational Studies

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-ggplot2 >= 3.0.0

%description
Generates weights to form equivalent groups in observational studies with
point or longitudinal treatments by easing and extending the functionality
of the R packages 'twang' for generalized boosted modeling (McCaffrey,
Ridgeway & Morral, 2004) <doi:10.1037/1082-989X.9.4.403>, 'CBPS' for
covariate balancing propensity score weighting (Imai & Ratkovic, 2014)
<doi:10.1111/rssb.12027>, 'ebal' for entropy balancing (Hainmueller, 2012)
<doi:10.1093/pan/mpr025>, 'optweight' for optimization-based weights
(Zubizarreta, 2015) <doi:10.1080/01621459.2015.1023805>, 'ATE' for
empirical balancing calibration weighting (Chan, Yam, & Zhang, 2016)
<doi:10.1111/rssb.12129>, and 'SuperLearner' for stacked machine
learning-based propensity scores (Pirracchio, Petersen, & van der Laan,
2015) <doi:10.1093/aje/kwu253>. Also allows for assessment of weights and
checking of covariate balance by interfacing directly with 'cobalt'.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
