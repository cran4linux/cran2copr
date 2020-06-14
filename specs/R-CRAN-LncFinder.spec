%global packname  LncFinder
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          2%{?dist}
Summary:          LncRNA Identification and Analysis Using Heterologous Features

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-caret >= 6.0.71
BuildRequires:    R-CRAN-seqinr >= 2.1.3
BuildRequires:    R-parallel >= 2.1.0
BuildRequires:    R-CRAN-e1071 >= 1.0
Requires:         R-CRAN-caret >= 6.0.71
Requires:         R-CRAN-seqinr >= 2.1.3
Requires:         R-parallel >= 2.1.0
Requires:         R-CRAN-e1071 >= 1.0

%description
Long non-coding RNAs identification and analysis. Default models are
trained with human, mouse and wheat datasets by employing SVM. Features
are based on intrinsic composition of sequence, EIIP value (electron-ion
interaction pseudopotential), and secondary structure. This package can
also extract other classic features and build new classifiers. Reference:
Han SY., Liang YC., Li Y., et al. (2018) <doi:10.1093/bib/bby065>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
