%global __brp_check_rpaths %{nil}
%global packname  extraterrestrial
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Astrobiology Equations Estimating Extraterrestrial Life

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
Finding life outside the planet Earth several is the ultimate goal of an
astrobiologist. Using known astronomical measurements and assumptions the
probability of extraterrestrial life existence could be estimated.
Equations such as the Drake equation (1961) as stated in the paper of
Molina (2019) <arXiv:1912.01783>, Seager (2013)
<https://www.space.com/22648-drake-equation-alien-life-seager.html> and
Foucher et al, (2017) <doi:10.3390/life7040040> are included in the
'extraterrestrial' package.

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
%{rlibdir}/%{packname}
