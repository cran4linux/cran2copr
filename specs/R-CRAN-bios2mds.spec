%global packname  bios2mds
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          3%{?dist}%{?buildtag}
Summary:          From Biological Sequences to Multidimensional Scaling

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
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
Utilities dedicated to the analysis of biological sequences by metric
MultiDimensional Scaling with projection of supplementary data. It
contains functions for reading multiple sequence alignment files,
calculating distance matrices, performing metric multidimensional scaling
and visualizing results.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/ex_class_file.csv
%doc %{rlibdir}/%{packname}/msa
%{rlibdir}/%{packname}/INDEX
