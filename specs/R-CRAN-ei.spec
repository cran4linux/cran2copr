%global packname  ei
%global packver   1.3-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.3
Release:          2%{?dist}%{?buildtag}
Summary:          Ecological Inference

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.5.0
Requires:         R-core >= 2.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-eiPack 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-ucminf 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-eiPack 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-plotrix 
Requires:         R-MASS 
Requires:         R-CRAN-ucminf 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-sp 

%description
Software accompanying Gary King's book: A Solution to the Ecological
Inference Problem. (1997). Princeton University Press. ISBN
978-0691012407.

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
