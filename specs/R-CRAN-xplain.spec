%global __brp_check_rpaths %{nil}
%global packname  xplain
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Providing Interactive Interpretations and Explanations ofStatistical Results

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-httr 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-httr 

%description
Allows to provide live interpretations and explanations of statistical
functions in R. These interpretations and explanations are shown when the
explained function is called by the user. They can interact with the
values of the explained function's actual results to offer relevant,
meaningful insights. The 'xplain' interpretations and explanations are
based on an easy-to-use XML format that allows to include R code to
interact with the returns of the explained function.

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
