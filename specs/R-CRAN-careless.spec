%global packname  careless
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          2%{?dist}%{?buildtag}
Summary:          Procedures for Computing Indices of Careless Responding

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-psych 
Requires:         R-CRAN-psych 

%description
When taking online surveys, participants sometimes respond to items
without regard to their content. These types of responses, referred to as
careless or insufficient effort responding, constitute significant
problems for data quality, leading to distortions in data analysis and
hypothesis testing, such as spurious correlations. The 'R' package
'careless' provides solutions designed to detect such careless /
insufficient effort responses by allowing easy calculation of indices
proposed in the literature. It currently supports the calculation of
longstring, even-odd consistency, psychometric synonyms/antonyms,
Mahalanobis distance, and intra-individual response variability (also
termed inter-item standard deviation). For a review of these methods, see
Curran (2016) <doi:10.1016/j.jesp.2015.07.006>.

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
