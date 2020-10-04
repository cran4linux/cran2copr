%global packname  ldaPrototype
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
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
BuildRequires:    R-CRAN-batchtools >= 0.9.11
BuildRequires:    R-CRAN-dendextend 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-parallelMap 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-checkmate >= 1.8.5
Requires:         R-CRAN-lda >= 1.4.2
Requires:         R-CRAN-colorspace >= 1.4.1
Requires:         R-CRAN-fs >= 1.2.0
Requires:         R-CRAN-data.table >= 1.11.2
Requires:         R-CRAN-progress >= 1.1.1
Requires:         R-CRAN-batchtools >= 0.9.11
Requires:         R-CRAN-dendextend 
Requires:         R-CRAN-future 
Requires:         R-CRAN-parallelMap 
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

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
