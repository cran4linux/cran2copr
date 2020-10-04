%global packname  dosearch
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Causal Effect Identification from Multiple Incomplete DataSources

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.19
Requires:         R-CRAN-Rcpp >= 0.12.19

%description
Identification of causal effects from arbitrary observational and
experimental probability distributions via do-calculus and standard
probability manipulations using a search-based algorithm. Allows for the
presence of mechanisms related to selection bias (Bareinboim, E. and Tian,
J. (2015) <http://ftp.cs.ucla.edu/pub/stat_ser/r445.pdf>),
transportability (Bareinboim, E. and Pearl, J. (2014)
<http://ftp.cs.ucla.edu/pub/stat_ser/r443.pdf>), missing data (Mohan, K.
and Pearl, J. and Tian., J. (2013)
<http://ftp.cs.ucla.edu/pub/stat_ser/r410.pdf>) and arbitrary combinations
of these. Also supports identification in the presence of context-specific
independence (CSI) relations through labeled directed acyclic graphs
(LDAG). For details on CSIs see Corander et al. (2019)
<doi:10.1016/j.apal.2019.04.004>. For further information on the
search-based approach see Tikka et al. (2019) <arXiv:1902.01073>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
