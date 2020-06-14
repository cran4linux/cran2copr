%global packname  EloChoice
%global packver   0.29.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.29.4
Release:          2%{?dist}
Summary:          Preference Rating for Visual Stimuli Based on Elo Ratings

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-psychotools 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-psychotools 
Requires:         R-CRAN-Rdpack 

%description
Allows calculating global scores for characteristics of visual stimuli as
assessed by human raters. Stimuli are presented as sequence of pairwise
comparisons ('contests'), during each of which a rater expresses
preference for one stimulus over the other (forced choice). The algorithm
for calculating global scores is based on Elo rating, which updates
individual scores after each single pairwise contest. Elo rating is widely
used to rank chess players according to their performance. Its core
feature is that dyadic contests with expected outcomes lead to smaller
changes of participants' scores than outcomes that were unexpected. As
such, Elo rating is an efficient tool to rate individual stimuli when a
large number of such stimuli are paired against each other in the context
of experiments where the goal is to rank stimuli according to some
characteristic of interest. Clark et al (2018)
<doi:10.1371/journal.pone.0190393> provide details.

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
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
