%global __brp_check_rpaths %{nil}
%global packname  TFMPvalue
%global packver   0.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.8
Release:          3%{?dist}%{?buildtag}
Summary:          Efficient and Accurate P-Value Computation for Position WeightMatrices

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildRequires:    R-CRAN-Rcpp >= 0.11.1
Requires:         R-CRAN-Rcpp >= 0.11.1

%description
In putative Transcription Factor Binding Sites (TFBSs) identification from
sequence/alignments, we are interested in the significance of certain
match score. TFMPvalue provides the accurate calculation of P-value with
score threshold for Position Weight Matrices, or the score with given
P-value. It is an interface to code originally made available by Helene
Touzet and Jean-Stephane Varre, 2007, Algorithms Mol Biol:2, 15. Touzet
and Varre (2007) <DOI:10.1186/1748-7188-2-15>.

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
%doc %{rlibdir}/%{packname}/TFMPvalueBuild
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
