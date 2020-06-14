%global packname  lmds
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Landmark Multi-Dimensional Scaling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dynutils >= 1.0.3
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-dynutils >= 1.0.3
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-irlba 
Requires:         R-Matrix 

%description
A fast dimensionality reduction method scaleable to large numbers of
samples. Landmark Multi-Dimensional Scaling (LMDS) is an extension of
classical Torgerson MDS, but rather than calculating a complete distance
matrix between all pairs of samples, only the distances between a set of
landmarks and the samples are calculated.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
