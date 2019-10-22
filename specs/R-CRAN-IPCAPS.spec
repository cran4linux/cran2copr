%global packname  IPCAPS
%global packver   1.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          1%{?dist}
Summary:          Iterative Pruning to Capture Population Structure

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.4.0
Requires:         R-core >= 3.2.4.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-KRIS 
BuildRequires:    R-CRAN-fpc 
BuildRequires:    R-CRAN-LPCM 
BuildRequires:    R-CRAN-apcluster 
BuildRequires:    R-CRAN-Rmixmod 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-KRIS 
Requires:         R-CRAN-fpc 
Requires:         R-CRAN-LPCM 
Requires:         R-CRAN-apcluster 
Requires:         R-CRAN-Rmixmod 

%description
An unsupervised clustering algorithm based on iterative pruning is for
capturing population structure. This version supports ordinal data which
can be applied directly to SNP data to identify fine-level population
structure and it is built on the iterative pruning Principal Component
Analysis ('ipPCA') algorithm as explained in Intarapanich et al. (2009)
<doi:10.1186/1471-2105-10-382>. The 'IPCAPS' involves an iterative process
using multiple splits based on multivariate Gaussian mixture modeling of
principal components and 'Expectation-Maximization' clustering as
explained in Lebret et al. (2015) <doi:10.18637/jss.v067.i06>. In each
iteration, rough clusters and outliers are also identified using the
function rubikclust() from the R package 'KRIS'.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
