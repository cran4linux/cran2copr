%global packname  regtomean
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Regression Toward the Mean

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-formattable 
BuildRequires:    R-CRAN-effsize 
BuildRequires:    R-CRAN-mefa 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-sjPlot 
BuildRequires:    R-CRAN-sjmisc 
BuildRequires:    R-CRAN-sjlabelled 
Requires:         R-CRAN-formattable 
Requires:         R-CRAN-effsize 
Requires:         R-CRAN-mefa 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-sjPlot 
Requires:         R-CRAN-sjmisc 
Requires:         R-CRAN-sjlabelled 

%description
In repeated measures studies with extreme large or small values it is
common that the subjects measurements on average are closer to the mean of
the basic population. Interpreting possible changes in the mean in such
situations can lead to biased results since the values were not randomly
selected, they come from truncated sampling. This method allows to
estimate the range of means where treatment effects are likely to occur
when regression toward the mean is present. Ostermann, T., Willich, Stefan
N. & Luedtke, Rainer. (2008). Regression toward the mean - a detection
method for unknown population mean based on Mee and Chua's algorithm. BMC
Medical Research Methodology.<doi:10.1186/1471-2288-8-52>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
