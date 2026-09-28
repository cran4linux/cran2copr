%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  myman
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Draw from Sequence of 'My Man' Posts by Kevin Kruse

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch

%description
Starting on the afternoon of July 17, 2026, Kevin Kruse fired off an
astonishing array of 'BlueSky' replies to an initial post of his featuring
a certain government figure:
<https://bsky.app/profile/did:plc:cnpe7qvcyjrhm6w7w7e4atur/post/3mqum4mxsuk2g>.
This lasted a week and generated nearly seven hundred posts. A second wave
started on August 12, 2026, with this post:
<https://bsky.app/profile/kevinmkruse.bsky.social/post/3mstvbjpagc2a>. A
third wave started on August 17, 2026, with
<https://bsky.app/profile/kevinmkruse.bsky.social/post/3mtcpiw7gi22j>.  A
fourth wave started on August 27, 2026, with
<https://bsky.app/profile/kevinmkruse.bsky.social/post/3mu3pugs2yk2f>. A
fifth wave ran on August 30, 2026, beginning with
<https://bsky.app/profile/kevinmkruse.bsky.social/post/3mudbzy5ksk25>.  A
sixth wave started September 4, 2026, with
<https://bsky.app/profile/kevinmkruse.bsky.social/post/3muparqtdkk2w>. A
seventh wave started September 12, 2026, with
<https://bsky.app/profile/kevinmkruse.bsky.social/post/3mvdol6xu5k2s>.
All of the over fourteen hundred posts from these series start with 'My
man ...' and make for excellent input to a 'fortunes'-like package. So
this small package obliges and offers a random draw each time its myman()
function is called.  The overall package structure follows package
'fortunes', and 'atrrr' was used to (bulk-)retrieve posts. Neither package
is required to run this package to display random selections.

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
