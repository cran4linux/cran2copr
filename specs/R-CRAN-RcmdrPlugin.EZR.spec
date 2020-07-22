%global packname  RcmdrPlugin.EZR
%global packver   1.51
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.51
Release:          1%{?dist}
Summary:          R Commander Plug-in for the EZR (Easy R) Package

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rcmdr >= 2.6.0
BuildRequires:    R-CRAN-readstata13 
Requires:         R-CRAN-Rcmdr >= 2.6.0
Requires:         R-CRAN-readstata13 

%description
EZR (Easy R) adds a variety of statistical functions, including survival
analyses, ROC analyses, metaanalyses, sample size calculation, and so on,
to the R commander. EZR enables point-and-click easy access to statistical
functions, especially for medical statistics. EZR is platform-independent
and runs on Windows, Mac OS X, and UNIX. Its complete manual is available
only in Japanese (Chugai Igakusha, ISBN: 978-4-498-10901-8 or Nankodo,
ISBN: 978-4-524-26158-1), but an report that introduced the investigation
of EZR was published in Bone Marrow Transplantation (Nature Publishing
Group) as an Open article. This report can be used as a simple manual. It
can be freely downloaded from the journal website as shown below. This
report has been cited in more than 3,000 scientific articles.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
xvfb-run %{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
