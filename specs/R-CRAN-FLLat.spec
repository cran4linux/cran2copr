%global __brp_check_rpaths %{nil}
%global packname  FLLat
%global packver   1.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Fused Lasso Latent Feature Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-gplots 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-gplots 

%description
Fits the Fused Lasso Latent Feature model, which is used for modeling
multi-sample aCGH data to identify regions of copy number variation (CNV).
Produces a set of features that describe the patterns of CNV and a set of
weights that describe the composition of each sample.  Also provides
functions for choosing the optimal tuning parameters and the appropriate
number of features, and for estimating the false discovery rate.

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
