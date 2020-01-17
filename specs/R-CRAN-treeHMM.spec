%global packname  treeHMM
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Tree Structured Hidden Markov Model

License:          GPL (>= 2.0.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-PRROC 
Requires:         R-Matrix 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-future 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-PRROC 

%description
Used for Inference, Prediction and Parameter learning for tree structured
Hidden Markov Model. The package propose a new architecture of Hidden
Markov Model(HMM) known as Tree Structured HMM which could be used in
various applications which involves graphs, trees etc.

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
