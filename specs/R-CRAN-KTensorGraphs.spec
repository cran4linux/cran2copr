%global packname  KTensorGraphs
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Co-Tucker3 Analysis of Two Sequences of Matrices

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Provides a function called COTUCKER3() (Co-Inertia Analysis + Tucker3
method) which performs a Co-Tucker3 analysis of two sequences of matrices,
as well as other functions called PCA() (Principal Component Analysis) and
BGA() (Between-Groups Analysis), which perform analysis of one matrix,
COIA() (Co-Inertia Analysis), which performs analysis of two matrices,
PTA() (Partial Triadic Analysis) and TUCKER3(), which perform analysis of
a sequence of matrices, and BGCOIA() (Between-Groups Co-Inertia Analysis),
STATICO() (STATIS method + Co-Inertia Analysis), COSTATIS() (Co-Inertia
Analysis + STATIS method), which also perform analysis of two sequences of
matrices.

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
%{rlibdir}/%{packname}/INDEX
