%global packname  bios2mds
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}
Summary:          From BIOlogical Sequences to MultiDimensional Scaling

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12
Requires:         R-core >= 2.12
BuildArch:        noarch
BuildRequires:    R-CRAN-amap 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-rgl 
Requires:         R-CRAN-amap 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-scales 
Requires:         R-cluster 
Requires:         R-CRAN-rgl 

%description
Bios2mds is primarily dedicated to the analysis of biological sequences by
metric MultiDimensional Scaling with projection of supplementary data. It
contains functions for reading multiple sequence alignment files,
calculating distance matrices, performing metric multidimensional scaling
and visualizing results.

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
%doc %{rlibdir}/%{packname}/csv
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/msa
%{rlibdir}/%{packname}/INDEX
