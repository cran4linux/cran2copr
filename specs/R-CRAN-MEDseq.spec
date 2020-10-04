%global packname  MEDseq
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          2%{?dist}%{?buildtag}
Summary:          Mixtures of Exponential-Distance Models with Covariates

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-seriation 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-TraMineR 
BuildRequires:    R-CRAN-WeightedCluster 
Requires:         R-cluster 
Requires:         R-CRAN-matrixStats 
Requires:         R-nnet 
Requires:         R-CRAN-seriation 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-TraMineR 
Requires:         R-CRAN-WeightedCluster 

%description
Implements a model-based clustering method for categorical life-course
sequences relying on mixtures of exponential-distance models introduced by
Murphy et al. (2019) <arXiv:1908.07963>. A range of flexible precision
parameter settings corresponding to weighted generalisations of the
Hamming distance metric are considered, along with the potential inclusion
of a noise component. Gating covariates can be supplied in order to relate
sequences to baseline characteristics. Sampling weights are also
accommodated. The models are fitted using the EM algorithm and tools for
visualising the results are also provided.

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

%files
%{rlibdir}/%{packname}
