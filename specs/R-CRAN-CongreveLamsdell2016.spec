%global __brp_check_rpaths %{nil}
%global packname  CongreveLamsdell2016
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Distance Metrics for Trees Generated by Congreve and Lamsdell

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Ternary 
Requires:         R-CRAN-Ternary 

%description
Includes the 100 datasets simulated by Congreve and Lamsdell (2016)
<doi:10.1111/pala.12236>, and analyses of the partition and quartet
distance of reconstructed trees from the generative tree, as analysed by
Smith (2019) <doi:10.1098/rsbl.2018.0632>.

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
