%global packname  DiPhiSeq
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}
Summary:          Robust Tests for Differential Dispersion and DifferentialExpression in RNA-Sequencing Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.1.0
Requires:         R-stats >= 3.1.0

%description
Implements the algorithm described in Jun Li and Alicia T. Lamere,
"DiPhiSeq: Robust comparison of expression levels on RNA-Seq data with
large sample sizes" (Unpublished). Detects not only genes that show
different average expressions ("differential expression", DE), but also
genes that show different diversities of expressions in different groups
("differentially dispersed", DD). DD genes can be important clinical
markers. 'DiPhiSeq' uses a redescending penalty on the quasi-likelihood
function, and thus has superior robustness against outliers and other
noise. Updates from version 0.1.0: (1) Added the option of using adaptive
initial value for phi. (2) Added a function for estimating the proportion
of outliers in the data. (3) Modified the input parameter names for
clarity, and modified the output format for the main function.

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
%{rlibdir}/%{packname}/INDEX
