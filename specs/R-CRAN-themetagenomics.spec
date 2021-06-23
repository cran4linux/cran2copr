%global __brp_check_rpaths %{nil}
%global packname  themetagenomics
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Exploring Thematic Structure and Predicted Functionality of 16srRNA Amplicon Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.5
Requires:         R-core >= 3.2.5
BuildRequires:    R-CRAN-plotly >= 4.5.6
BuildRequires:    R-CRAN-rstan >= 2.14.0
BuildRequires:    R-CRAN-stm >= 1.1.4
BuildRequires:    R-CRAN-lme4 >= 1.1.12
BuildRequires:    R-CRAN-shiny >= 1.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.3
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lda 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-stats4 
Requires:         R-CRAN-plotly >= 4.5.6
Requires:         R-CRAN-rstan >= 2.14.0
Requires:         R-CRAN-stm >= 1.1.4
Requires:         R-CRAN-lme4 >= 1.1.12
Requires:         R-CRAN-shiny >= 1.0.0
Requires:         R-CRAN-Rcpp >= 0.11.3
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lda 
Requires:         R-Matrix 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-stats4 

%description
A means to explore the structure of 16S rRNA surveys using a Structural
Topic Model coupled with functional prediction. The user provides an
abundance table, sample metadata, and taxonomy information, and
themetagenomics infers associations between topics and sample features, as
well as topics and predicted functional content. Functional prediction can
be accomplished via Tax4Fun (for Silva references) and PICRUSt (for
GreenGeenes references). See <doi:10.1371/journal.pone.0219235>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/references
%{rlibdir}/%{packname}/testdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
