%global __brp_check_rpaths %{nil}
%global packname  signalHsmm
%global packver   1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5
Release:          3%{?dist}%{?buildtag}
Summary:          Predict Presence of Signal Peptides

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-seqinr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-graphics 
Requires:         R-CRAN-seqinr 
Requires:         R-CRAN-shiny 
Requires:         R-stats 
Requires:         R-utils 

%description
Predicts the presence of signal peptides in eukaryotic protein using
hidden semi-Markov models. The implemented algorithm can be accessed from
both the command line and GUI.

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
