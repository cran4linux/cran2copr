%global packname  BreakPoints
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}
Summary:          Identify Breakpoints in Series of Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-zoo 
Requires:         R-MASS 
Requires:         R-CRAN-zoo 

%description
Compute Buishand Range Test, Pettit Test, SNHT, Student t-test, and
Mann-Whitney Rank Test, to identify breakpoints in series. For all
functions NA is allowed. Since all of the mention methods identify only
one breakpoint in a series, a general function to look for N breakpoint is
given. Also, the Yamamoto test for climate jump is available.
Alexandersson, H. (1986) <doi:10.1002/joc.3370060607>, Buishand, T. (1982)
<doi:10.1016/0022-1694(82)90066-X>, Hurtado, S. I., Zaninelli, P. G., &
Agosta, E. A. (2020) <doi:10.1016/j.atmosres.2020.104955>, Mann, H. B.,
Whitney, D. R. (1947) <doi:10.1214/aoms/1177730491>, Pettitt, A. N. (1979)
<doi:10.2307/2346729>, Ruxton, G. D., jul (2006)
<doi:10.1093/beheco/ark016>, Yamamoto, R., Iwashima, T., Kazadi, S. N., &
Hoshiai, M. (1985) <doi:10.2151/jmsj1965.63.6_1157>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
