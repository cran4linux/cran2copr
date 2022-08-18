%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sotu
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          United States Presidential State of the Union Addresses

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-utils 
Requires:         R-utils 

%description
The President of the United States is constitutionally obligated to
provide a report known as the 'State of the Union'. The report summarizes
the current challenges facing the country and the president's upcoming
legislative agenda. While historically the State of the Union was often a
written document, in recent decades it has always taken the form of an
oral address to a joint session of the United States Congress. This
package provides the raw text from every such address with the intention
of being used for meaningful examples of text analysis in R. The corpus is
well suited to the task as it is historically important, includes material
intended to be read and material intended to be spoken, and it falls in
the public domain. As the corpus spans over two centuries it is also a
good test of how well various methods hold up to the idiosyncrasies of
historical texts. Associated data about each address, such as the year,
president, party, and format, are also included.

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
