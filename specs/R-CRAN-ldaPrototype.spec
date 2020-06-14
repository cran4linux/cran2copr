%global packname  ldaPrototype
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}
Summary:          Prototype of Multiple Latent Dirichlet Allocation Runs

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 1.8.5
BuildRequires:    R-CRAN-lda >= 1.4.2
BuildRequires:    R-CRAN-colorspace >= 1.4.1
BuildRequires:    R-CRAN-fs >= 1.2.0
BuildRequires:    R-CRAN-data.table >= 1.11.2
BuildRequires:    R-CRAN-progress >= 1.1.1
BuildRequires:    R-CRAN-dendextend 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-checkmate >= 1.8.5
Requires:         R-CRAN-lda >= 1.4.2
Requires:         R-CRAN-colorspace >= 1.4.1
Requires:         R-CRAN-fs >= 1.2.0
Requires:         R-CRAN-data.table >= 1.11.2
Requires:         R-CRAN-progress >= 1.1.1
Requires:         R-CRAN-dendextend 
Requires:         R-stats 
Requires:         R-utils 

%description
Determine a Prototype from a number of runs of Latent Dirichlet Allocation
(LDA) measuring its similarities with S-CLOP: A procedure to select the
LDA run with highest mean pairwise similarity, which is measured by S-CLOP
(Similarity of multiple sets by Clustering with Local Pruning), to all
other runs. LDA runs are specified by its assignments leading to
estimators for distribution parameters. Repeated runs lead to different
results, which we encounter by choosing the most representative LDA run as
prototype.

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
