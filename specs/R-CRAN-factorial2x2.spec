%global __brp_check_rpaths %{nil}
%global packname  factorial2x2
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Design and Analysis of a 2x2 Factorial Trial

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-survival 
Requires:         R-stats 
Requires:         R-CRAN-mvtnorm 

%description
Used for the design and analysis of a 2x2 factorial trial for a
time-to-event endpoint.  It performs power calculations and significance
testing as well as providing estimates of the relevant hazard ratios and
the corresponding 95% confidence intervals.  Important reference papers
include Slud EV. (1994) <https://www.ncbi.nlm.nih.gov/pubmed/8086609> Lin
DY, Gong J, Gallo P, Bunn PH, Couper D. (2016) <DOI:10.1111/biom.12507>
Leifer ES, Troendle JF, Kolecki A, Follmann DA. (2020)
<https://github.com/EricSLeifer/factorial2x2/blob/master/Leifer%20et%20al.%20paper.pdf>.

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
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
