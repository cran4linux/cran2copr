%global __brp_check_rpaths %{nil}
%global packname  TTCA
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Transcript Time Course Analysis

License:          EUPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-tcltk2 
BuildRequires:    R-CRAN-RISmed 
BuildRequires:    R-CRAN-VennDiagram 
BuildRequires:    R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-tcltk2 
Requires:         R-CRAN-RISmed 
Requires:         R-CRAN-VennDiagram 
Requires:         R-MASS 

%description
The analysis of microarray time series promises a deeper insight into the
dynamics of the cellular response following stimulation. A common
observation in this type of data is that some genes respond with quick,
transient dynamics, while other genes change their expression slowly over
time. The existing methods for detecting significant expression dynamics
often fail when the expression dynamics show a large heterogeneity.
Moreover, these methods often cannot cope with irregular and sparse
measurements. The method proposed here is specifically designed for the
analysis of perturbation responses. It combines different scores to
capture fast and transient dynamics as well as slow expression changes,
and performs well in the presence of low replicate numbers and irregular
sampling times. The results are given in the form of tables including
links to figures showing the expression dynamics of the respective
transcript. These allow to quickly recognise the relevance of detection,
to identify possible false positives and to discriminate early and late
changes in gene expression. An extension of the method allows the analysis
of the expression dynamics of functional groups of genes, providing a
quick overview of the cellular response. The performance of this package
was tested on microarray data derived from lung cancer cells stimulated
with epidermal growth factor (EGF). Paper: Albrecht, Marco, et al.
(2017)<DOI:10.1186/s12859-016-1440-8>.

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
