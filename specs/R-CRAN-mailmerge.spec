%global __brp_check_rpaths %{nil}
%global packname  mailmerge
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Mail Merge Using R Markdown Documents and 'gmailr'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-commonmark 
BuildRequires:    R-CRAN-gmailr 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-googledrive 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-googlesheets4 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-miniUI 
Requires:         R-CRAN-commonmark 
Requires:         R-CRAN-gmailr 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-googledrive 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-googlesheets4 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-purrr 
Requires:         R-utils 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-miniUI 

%description
Perform a mail merge (mass email) using the message defined in markdown,
the recipients in a csv, and gmail as the mailing engine. With this
package you can parse markdown documents as the body of email, and the
'yaml' header to specify the subject line of the email.  Any '{}' braces
in the email will be encoded with 'glue::glue()'. You can preview the
email in the RStudio viewer pane, and send (draft) email using 'gmailr'.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
