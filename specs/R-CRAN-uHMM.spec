%global __brp_check_rpaths %{nil}
%global packname  uHMM
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Construct an Unsupervised Hidden Markov Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-tcltk2 
BuildRequires:    R-CRAN-tkrplot 
BuildRequires:    R-CRAN-HMM 
BuildRequires:    R-CRAN-clValid 
BuildRequires:    R-class 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-chron 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-tcltk 
Requires:         R-CRAN-tcltk2 
Requires:         R-CRAN-tkrplot 
Requires:         R-CRAN-HMM 
Requires:         R-CRAN-clValid 
Requires:         R-class 
Requires:         R-cluster 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-chron 

%description
Construct a Hidden Markov Model with states learnt by unsupervised
classification.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
xvfb-run %{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
