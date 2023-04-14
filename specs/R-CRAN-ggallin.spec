%global __brp_check_rpaths %{nil}
%global packname  ggallin
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Grab Bag of 'ggplot2' Functions

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-grid 
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-scales 
Requires:         R-grid 

%description
Extra geoms and scales for 'ggplot2', including geom_cloud(), a Normal
density cloud replacement for errorbars; transforms ssqrt_trans and
pseudolog10_trans, which are loglike but appropriate for negative data;
interp_trans() and warp_trans() which provide scale transforms based on
interpolation; and an infix compose operator for scale transforms.

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
