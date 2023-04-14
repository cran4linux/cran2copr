%global __brp_check_rpaths %{nil}
%global packname  pvclust
%global packver   2.2-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Hierarchical Clustering with P-Values via Multiscale BootstrapResampling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch

%description
An implementation of multiscale bootstrap resampling for assessing the
uncertainty in hierarchical cluster analysis. It provides SI (selective
inference) p-value, AU (approximately unbiased) p-value and BP (bootstrap
probability) value for each cluster in a dendrogram.

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
