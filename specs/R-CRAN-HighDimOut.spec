%global packname  HighDimOut
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Outlier Detection Algorithms for High-Dimensional Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-DMwR 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-DMwR 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-ggplot2 

%description
Three high-dimensional outlier detection algorithms and a outlier
unification scheme are implemented in this package. The angle-based
outlier detection (ABOD) algorithm is based on the work of Kriegel,
Schubert, and Zimek [2008]. The subspace outlier detection (SOD) algorithm
is based on the work of Kriegel, Kroger, Schubert, and Zimek [2009]. The
feature bagging-based outlier detection (FBOD) algorithm is based on the
work of Lazarevic and Kumar [2005]. The outlier unification scheme is
based on the work of Kriegel, Kroger, Schubert, and Zimek [2011].

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
