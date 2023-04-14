%global __brp_check_rpaths %{nil}
%global packname  ECLRMC
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Ensemble Correlation-Based Low-Rank Matrix Completion

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-softImpute 
Requires:         R-CRAN-softImpute 

%description
Ensemble correlation-based low-rank matrix completion method (ECLRMC) is
an extension to the LRMC based methods. Traditionally, the LRMC based
methods give identical importance to the whole data which results in
emphasizing on the commonality of the data and overlooking the subtle but
crucial differences. This method aims to overcome the equality assumption
problem that exists in the current LRMS based methods. Ensemble
correlation-based low-rank matrix completion (ECLRMC) takes consideration
of the specific characteristic of each sample and performs LRMC on the set
of samples with a strong correlation. It uses an ensemble learning method
to improve the imputation performance. Since each sample is analyzed
independently this method can be parallelized by distributing imputation
across many computation units or GPU platforms. This package provides
three different methods (LRMC, CLRMC and ECLRMC) for data imputation.
There is also an NRMS function for evaluating the result. Chen, Xiaobo, et
al (2017) <doi:10.1016/j.knosys.2017.06.010>.

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
